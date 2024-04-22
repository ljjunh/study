import { useState, useRef } from "react";
// 간단한 회원가입 폼
// 1. 이름
// 2. 생년월일
// 3. 국적
// 4. 자기소개

const Register = () => {
  //   const [name, setName] = useState("이름");
  //   const [birth, setBirth] = useState("");
  //   const [country, setCountry] = useState("");
  //   const [bio, setBio] = useState("");
  //state 하나로 통합
  const [input, setInput] = useState({
    name: "",
    birth: "",
    country: "",
    bio: "",
  });
  const countRef = useRef(0); // 값이 변경되도 리랜더링 시키지 않음
  //그래서 레퍼런스 오브젝트는 컴포넌트 내부에서 렌더링에 영향을 미치지 않아야 되는 변수를 생성할 때 활용 가능
  const inputRef = useRef();

  //핸들러 하나로 통합
  const onChange = (e) => {
    countRef.current++;
    console.log(countRef.current);
    setInput({
      ...input,
      [e.target.name]: e.target.value, //대괄호 열고 변수 넣으면 프로퍼티의 키가 됨
      //e.target.name엔 이벤트가 발생한 태그의 name속성에 설정된 값이 들어있음
    });
  };

  const onSubmit = () => {
    if (input.name === "") {
      // 이름을 입력하는 DOM 요소 포커스
      inputRef.current.focus();
    }
  };
  //   const onChangeName = (e) => {
  //     setInput({
  //       ...input, // 스프레드로 나머지input 안넣어주면 기존값들이 사라짐
  //       name: e.target.value,
  //     });
  //   };

  //   const onChangeDate = (e) => {
  //     setInput({
  //       ...input, // 스프레드로 나머지input 안넣어주면 기존값들이 사라짐
  //       birth: e.target.value,
  //     });
  //   };

  //   const onChangeCountry = (e) => {
  //     setInput({
  //       ...input, // 스프레드로 나머지input 안넣어주면 기존값들이 사라짐
  //       country: e.target.value,
  //     });
  //   };

  //   const onChangeBio = (e) => {
  //     setInput({
  //       ...input, // 스프레드로 나머지input 안넣어주면 기존값들이 사라짐
  //       bio: e.target.value,
  //     });
  //   };
  return (
    <div>
      <div>
        <input
          ref={inputRef}
          name="name"
          value={input.name}
          onChange={onChange}
          placeholder={"이름"}
        />
        {input.name}
      </div>
      <div>
        <input
          name="birth"
          value={input.birth}
          onChange={onChange}
          type="date"
        />
        {input.birth}
      </div>
      <div>
        <select name="country" value={input.country} onChange={onChange}>
          <option value=""></option>
          <option value="kr">한국</option>
          <option value="us">미국</option>
          <option value="uk">영국</option>
        </select>
        {input.country}
      </div>
      <div>
        <textarea name="bio" value={input.bio} onChange={onChange}></textarea>
        {input.bio}
      </div>
      <button onClick={onSubmit}>제출</button>
    </div>
  );
};

export default Register;
