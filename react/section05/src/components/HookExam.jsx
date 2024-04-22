import useInput from "../hooks/useInput";

// 3가지 hook 관련 팁
// 1. 함수 컴포넌트, 커스텀 훅 내부에서만 호출 가능
// 2. 조건부로 호출될 수는 없다.
// 3. Custom Hook을 직접 만들 수 있다.
// 3.2 그냥 함수앞에 use키워드 써주면 됨

// const state = useState(); //함수 컴포넌트 외부에서 호출해서 에러

const HookExam = () => {
  const [input, onChange] = useInput();

  if (true) {
    console.log(input);
  }
  return (
    <div>
      <input value={input} onChange={onChange} />
      {input}
    </div>
  );
};

export default HookExam;
