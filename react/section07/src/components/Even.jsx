import { useEffect } from "react";
const Even = () => {
  useEffect(() => {
    // useEffect의 콜백함수가 반환하는 함수를 클린업, 정리함수라고 부름
    return () => {
      console.log("unmount");
    };
  }, []);
  // deps를 빈 배열로 전달하면 useEffect는 mount될때 실행이 되고
  // unmount될때는 콜백함수 안의 정리함수가 실행됨
  return <div>짝수입니다</div>;
};
export default Even;
