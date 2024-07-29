import { useCallback, useRef, useState } from "react";
export const WebcamRecorder: React.FC = () => {
  // 비디오 엘리먼트에 대한 참조
  const webcamRef = useRef<HTMLVideoElement>(null);
  // 웹캠 스트림을 저장할 상태
  const [webcamStream, setWebcamStream] = useState<MediaStream | null>(null);
  // 좌우반전 상태
  const [isMirrored, setIsMirrored] = useState<boolean>(false);

  //  녹화 기능
  // MediaRecorder 참조
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  // 녹화 중 여부 상태
  const [isRecording, setIsRecording] = useState<boolean>(false);
  // 녹화된 비디오 데이터 청크 상태
  const [recordedChunks, setRecordedChunks] = useState<Blob[]>([]);

  // 웹캠 시작 함수
  const startWebCam = async (): Promise<void> => {
    try {
      const originalStream = await navigator.mediaDevices.getUserMedia({
        video: true,
        audio: true,
      });

      const videoTrack = originalStream.getVideoTracks()[0];
      const { width, height } = videoTrack.getSettings();

      const canvas = document.createElement("canvas");
      canvas.width = width!;
      canvas.height = height!;
      const ctx = canvas.getContext("2d")!;

      const video = document.createElement("video");
      video.srcObject = originalStream;
      video.play();

      video.onplaying = () => {
        setInterval(() => {
          ctx.save();
          ctx.scale(-1, 1);
          ctx.drawImage(video, -width!, 0, width!, height!);
          ctx.restore();
        }, 1000 / 30); // 30 FPS
      };

      const flippedStream = canvas.captureStream(30);

      // 오디오 트랙을 flippedStream에 추가
      originalStream.getAudioTracks().forEach((track) => {
        flippedStream.addTrack(track);
      });

      if (webcamRef.current) {
        webcamRef.current.srcObject = flippedStream;
      }
      setWebcamStream(flippedStream);
    } catch (error: unknown) {
      console.error("웹캠 접근 오류:", error);
    }
  };
  // // 좌우반전 토글 함수
  // const toggleMirror = (): void => {
  //   setIsMirrored((prev: boolean) => !prev);
  // };

  // 녹화 시작 함수
  const startRecording = useCallback((): void => {
    if (webcamStream) {
      const mediaRecorder: MediaRecorder = new MediaRecorder(webcamStream);
      mediaRecorderRef.current = mediaRecorder;

      // 녹화 시작 시 호출되는 이벤트 핸들러
      mediaRecorder.onstart = () => {
        setIsRecording(true);
        setRecordedChunks([]);
      };

      // 녹화 데이터 사용 가능할 때 호출되는 이벤트 핸들러
      mediaRecorder.ondataavailable = (e: BlobEvent) => {
        if (e.data.size > 0) {
          setRecordedChunks((prev: Blob[]) => [...prev, e.data]);
        }
      };

      // 녹화 중지 시 호출되는 이벤트 핸들러
      mediaRecorder.onstop = () => {
        setIsRecording(false);
      };

      // 녹화 시작
      mediaRecorder.start();
    }
  }, [webcamStream]);

  // 녹화 중지 함수
  const stopRecording = useCallback((): void => {
    if (mediaRecorderRef.current) {
      mediaRecorderRef.current.stop();
    }
  }, []);

  // 녹화본 저장 함수
  const saveRecording = useCallback((): void => {
    // 녹화된 데이터가 없으면 함수 종료
    if (recordedChunks.length === 0) return;

    // MediaRecorder가 녹화 중 주기적으로 ondataavailable 이벤트를 발생시킴
    // 그래서 각 이벤트마다 새로운 Blob이 생성되서 recordedChunks 배열에 추가됨
    // recordedChunks 배열의 모든 Blob을 하나로 합치고 타입을 video/mp4로 지정
    const blob: Blob = new Blob(recordedChunks, { type: "video/mp4" });
    // url 생성
    const url: string = URL.createObjectURL(blob);

    const a: HTMLAnchorElement = document.createElement("a");
    document.body.appendChild(a);
    a.style.display = "none";
    a.href = url;
    a.download = "recorded_video.mp4";
    // a태그를 만들고 사용자한테 안보이게 한다음
    // a.click()으로 프로그래매틱 클릭
    a.click();
    // 생성된 url 해제
    window.URL.revokeObjectURL(url);
    // 생성된 a태그 제거
    document.body.removeChild(a);
  }, [recordedChunks]);

  return (
    <div>
      <video
        ref={webcamRef}
        autoPlay
        muted
        // style={{ transform: isMirrored ? "scaleX(1)" : "scaleX(-1)" }}
      />
      <button onClick={startWebCam}>카메라 켜기</button>
      {/* <button onClick={toggleMirror}>
        {isMirrored ? "좌우반전 해제" : "좌우반전 적용"}
      </button> */}
      <button onClick={isRecording ? stopRecording : startRecording}>
        {isRecording ? "녹화 중지" : "녹화 시작"}
      </button>
      {recordedChunks.length > 0 && (
        <button onClick={saveRecording}>녹화본 저장</button>
      )}
    </div>
  );
};
