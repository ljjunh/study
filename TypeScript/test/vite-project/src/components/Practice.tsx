import React, { useEffect, useRef, useState } from "react";
import { useParams } from "react-router-dom";
import YouTube from "react-youtube";
import {
  PoseLandmarker,
  FilesetResolver,
  DrawingUtils,
  NormalizedLandmark,
} from "@mediapipe/tasks-vision";

export const Practice: React.FC = () => {
  const { videoId } = useParams<{ videoId: string }>();
  const videoRef = useRef<HTMLVideoElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [poseLandmarker, setPoseLandmarker] = useState<PoseLandmarker | null>(
    null
  );
  const [webcamError, setWebcamError] = useState<string | null>(null);

  useEffect(() => {
    const initializePoseLandmarker = async () => {
      try {
        const vision = await FilesetResolver.forVisionTasks(
          "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0/wasm"
        );
        const poseLandmarker = await PoseLandmarker.createFromOptions(vision, {
          baseOptions: {
            modelAssetPath: `https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_full/float16/1/pose_landmarker_full.task`,
            delegate: "CPU",
          },
          runningMode: "VIDEO",
          numPoses: 1,
        });
        setPoseLandmarker(poseLandmarker);
      } catch (error) {
        console.error("Error initializing PoseLandmarker:", error);
      }
    };

    initializePoseLandmarker();
  }, []);

  useEffect(() => {
    enableCam();
  }, []);

  const enableCam = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: "user", width: 640, height: 360 },
      });
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        videoRef.current.onloadedmetadata = () => {
          videoRef.current?.play();
        };
      }
      setWebcamError(null);
    } catch (err) {
      console.error("Error accessing the webcam:", err);
      setWebcamError(
        "웹캠에 접근할 수 없습니다. 브라우저 설정에서 권한을 확인해주세요."
      );
    }
  };

  const drawPose = (
    canvasCtx: CanvasRenderingContext2D,
    landmarks: NormalizedLandmark[][],
    color: string
  ) => {
    const drawingUtils = new DrawingUtils(canvasCtx);
    for (const landmark of landmarks) {
      drawingUtils.drawLandmarks(landmark, {
        radius: (data: NormalizedLandmark) =>
          DrawingUtils.lerp(data.z, -0.15, 0.1, 5, 1),
        color: color,
      });
      drawingUtils.drawConnectors(landmark, PoseLandmarker.POSE_CONNECTIONS, {
        color: color,
      });
    }
  };

  const detectAndDraw = async () => {
    if (!poseLandmarker || !videoRef.current || !canvasRef.current) return;

    const canvasCtx = canvasRef.current.getContext("2d");
    if (!canvasCtx) return;

    const startTimeMs = performance.now();

    // 웹캠 포즈 감지
    const results = await poseLandmarker.detectForVideo(
      videoRef.current,
      startTimeMs
    );

    canvasCtx.clearRect(
      0,
      0,
      canvasRef.current.width,
      canvasRef.current.height
    );

    // 웹캠 비디오를 캔버스에 그리기
    canvasCtx.drawImage(
      videoRef.current,
      0,
      0,
      canvasRef.current.width,
      canvasRef.current.height
    );

    // 포즈 그리기 (빨간색)
    drawPose(canvasCtx, results.landmarks, "red");

    requestAnimationFrame(detectAndDraw);
  };

  useEffect(() => {
    if (poseLandmarker) {
      detectAndDraw();
    }
  }, [poseLandmarker]);

  const opts = {
    height: "360",
    width: "640",
    playerVars: {
      autoplay: 0,
    },
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        width: "100%",
        maxWidth: "1300px",
        margin: "0 auto",
      }}
    >
      {webcamError && (
        <div style={{ color: "red", marginBottom: "10px" }}>{webcamError}</div>
      )}
      <div
        style={{
          display: "flex",
          justifyContent: "space-around",
          width: "100%",
        }}
      >
        <div style={{ width: "640px", height: "360px", position: "relative" }}>
          <YouTube videoId={videoId} opts={opts} />
        </div>
        <div style={{ width: "640px", height: "360px", position: "relative" }}>
          <canvas
            ref={canvasRef}
            width={640}
            height={360}
            style={{ position: "absolute", top: 0, left: 0, zIndex: 1 }}
          />
          <video
            ref={videoRef}
            style={{
              width: "640px",
              height: "360px",
              position: "absolute",
              top: 0,
              left: 0,
            }}
            autoPlay
            playsInline
          />
        </div>
      </div>
    </div>
  );
};

export default Practice;
