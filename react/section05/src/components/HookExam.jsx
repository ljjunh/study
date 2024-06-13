import useInput from "../hooks/useInput";
// 3가지 hook 관련 팁
// 1. 함수 컴포넌트, 커스텀 훅 내부에서만 호출 가능
// const state = useState(); 에러

// 2. 조건부로 호출될 수는 없다
// 조건부로 호출할 경우 서로 다른 훅들의 호출 순서가 꼬여 오류가 발생할 수 있어서

// 3. Custom Hook을 직접 만들 수 있다.(use키워드 사용해야함)
// 보통 컴포넌트에 안넣고 hooks폴더 안에 커스텀훅 파일로 저장

const HookExam = () => {
  // if (true) { // 조건부로 호출될 수 없음
  //   const state = useState();
  // }
  const [input, onChange] = useInput();
  const [input2, onChange2] = useInput();
  return (
    <div>
      <input value={input} onChange={onChange} />
      {input}
      <input value={input2} onChange={onChange2} />
      {input2}
    </div>
  );
};
export default HookExam;
