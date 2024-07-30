import React, { useEffect, useRef, useState } from "react";
import {
  PoseLandmarker,
  FilesetResolver,
  DrawingUtils,
} from "@mediapipe/tasks-vision";

const PoseLandmarkerComponent: React.FC = () => {
  const videoRef = useRef<HTMLVideoElement>(null); // 비디오 참조
  const canvasRef = useRef<HTMLCanvasElement>(null); // 캔버스 참조
  const [poseLandmarker, setPoseLandmarker] = useState<any>(null); // poselandmarker 상태 관리
  const [webcamRunning, setWebcamRunning] = useState(false); // 웹캠 상태 관리

  // 컴포넌트 마운트 시 PoseLandmarker 초기화
  // 이 함수를 통해서 웹캠이 활성화 되면 즉시 포즈 감지를 시작할 수 있는 상태가 됨
  useEffect(() => {
    const initializePoseLandmarker = async () => {
      // MediaPipe 비전 태스크를 위한 파일셋 리졸버 생성
      const vision = await FilesetResolver.forVisionTasks(
        "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0/wasm"
      );

      //PoseLandmarker 인스턴스 생성 및 옵션 설정
      const poseLandmarker = await PoseLandmarker.createFromOptions(vision, {
        baseOptions: {
          // 사용할 포즈 감지 모델의 경로 지정. full 버전 모델 사용
          modelAssetPath: `https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_full/float16/1/pose_landmarker_full.task`,
          // GPU를 사용해서 연산 가속화
          // 나중에 GPU를 기본으로 두고 GPU 없는 컴터에서는 CPU사용하도록
          delegate: "GPU",
        },
        // 비디오 스트림에서 연속적으로 포즈를 감지하도록 설정
        runningMode: "VIDEO",
        // 한번에 최대 2개의 포즈를 감지하도록 설정
        numPoses: 2,
      });
      // 생성된 PoseLandmarker 인스턴스를 컴포넌트의 상태에 저장
      setPoseLandmarker(poseLandmarker);
    };

    initializePoseLandmarker();
  }, []);

  const enableCam = async () => {
    // poseLandmarker가 없으면 바로 중단
    if (!poseLandmarker) {
      console.log("poseLandmaker가 아직 생성되지 않음");
      return;
    }
    // 웹캠 상태를 토글(켜짐/꺼짐)
    setWebcamRunning((prev) => !prev);

    // 웹캠이 꺼져 있다면 켜기
    if (!webcamRunning) {
      // 비디오 스트림 요청
      const constraints = { video: true };
      const stream = await navigator.mediaDevices.getUserMedia(constraints);
      // 비디오 요소에 스트림 연결
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
      }
    }
  };

  const predictWebcam = () => {
    // 필요한 요소들이 모두 준비되지 않았으면 함수 중단)
    if (!poseLandmarker || !videoRef.current || !canvasRef.current) return;

    const canvasCtx = canvasRef.current.getContext("2d");
    if (!canvasCtx) return;

    // 캔버스에 그리기 위한 유틸리기 객체 생성
    const drawingUtils = new DrawingUtils(canvasCtx);
    const FPS = 30;
    const detectAndDraw = async () => {
      const startTimeMs = performance.now();
      // 비디오 프레임에서 포즈 감지
      const results = await poseLandmarker.detectForVideo(
        videoRef.current,
        startTimeMs
      );
      canvasCtx.save();
      // 이전 프레임 자르기
      canvasCtx.clearRect(
        0,
        0,
        canvasRef.current!.width,
        canvasRef.current!.height
      );
      // 캔버스 좌우 반전(웹캠 이미지랑 일치시키려고)
      canvasCtx.scale(-1, 1);
      canvasCtx.translate(-canvasRef.current!.width, 0);

      // 감지된 각 포즈의 랜드마크와 연결선 그리기
      for (const landmark of results.landmarks) {
        // 랜드마크 점 그리기
        drawingUtils.drawLandmarks(landmark, {
          radius: (data: any) =>
            DrawingUtils.lerp(data.from!.z, -0.15, 0.1, 5, 1),
        });
        // 랜드마크 간 연결선 그리기
        drawingUtils.drawConnectors(landmark, PoseLandmarker.POSE_CONNECTIONS);
      }
      canvasCtx.restore();

      // 웹캠이 실행 중이면 다음 프레임 처리를 위해 재귀 호출
      if (webcamRunning) {
        setTimeout(() => requestAnimationFrame(detectAndDraw), 1000 / FPS);
      }
    };

    detectAndDraw();
  };

  useEffect(() => {
    // 웹캠이 실행중이고 비디오 요소가 준비되었을때
    if (webcamRunning && videoRef.current) {
      // 비디오 데이터가 로드되면 포즈 감지 시작
      // loadeddata 이벤트는 비디오의 첫 프레임이 로드되었을 때 발생
      videoRef.current.addEventListener("loadeddata", predictWebcam);
    }
    // 클린업 함수
    return () => {
      if (videoRef.current) {
        videoRef.current.removeEventListener("loadeddata", predictWebcam);
      }
    };
  }, [webcamRunning]); // webcamRunning 상태가 변경될때마다 위 함수 실행

  return (
    <div>
      <button onClick={enableCam}>
        {webcamRunning ? "Disable" : "Enable"} Webcam
      </button>
      <div style={{ position: "relative" }}>
        <video
          ref={videoRef}
          style={{ width: "640px", height: "480px", transform: "scaleX(-1)" }}
          autoPlay
          playsInline
        />
        <canvas
          ref={canvasRef}
          width={640}
          height={480}
          style={{ position: "absolute", left: 0, top: 0 }}
        />
      </div>
    </div>
  );
};

export default PoseLandmarkerComponent;
