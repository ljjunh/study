/* eslint-disable */
// import해놓고 안쓰는거나 선언해놓고 안쓰는 변수들 warning으로 알려주는건데 귀찮아서 일단 끔

import "./App.css";
import { useState } from "react";

function App() {
  const [title, setTitle] = useState([
    "나1번 게시글",
    "가2번 게시글",
    "다3번 게시글",
  ]);
  const [like, setLike] = useState([0, 0, 0]);
  const [modal, setModal] = useState(false);
  const [titleIdx, setTitleIdx] = useState(0);
  const [userInput, setUserInput] = useState("");

  //날짜
  const [year, setYear] = useState([2024, 2023, 2023]);
  const [month, setMonth] = useState([3, 2, 1]);
  const [date, setDate] = useState([9, 8, 7]);
  const [hours, setHours] = useState([10, 9, 7]);
  const [minutes, setMinutes] = useState([45, 14, 2]);

  // 오름차순 정렬
  const sortList = () => {
    let copy = [...title];
    copy.sort();
    setTitle(copy);
  };

  // 좋아요 수 증가
  const incrementLike = (idx, event) => {
    event.stopPropagation();
    let copy = [...like];
    copy[idx]++;
    setLike(copy);
  };

  // 모달창 보여주기/숨기기
  const showModal = (idx) => {
    setModal(!modal);
    setTitleIdx(idx);
  };

  // 게시글 삭제
  const deleteArticle = (idx) => {
    let copy = [...title];
    copy.splice(idx, 1);
    setTitle(copy);
  };
  // 사용자 입력값 저장
  const createUserInput = (event) => {
    setUserInput(event.target.value);
  };

  // 게시글 생성
  const createArticle = () => {
    if (userInput !== "") {
      let copy = [...title];
      copy.unshift(userInput);
      setTitle(copy);
      let tmp = [...like];
      tmp.unshift(0);
      setLike(tmp);
      // 날짜 시간 저장
      const now = new Date();
      let copyYear = [...year];
      copyYear.unshift(now.getFullYear());
      setYear(copyYear);

      let copyMonth = [...month];
      copyMonth.unshift(now.getMonth() + 1);
      setMonth(copyMonth);

      let copyDate = [...date];
      copyDate.unshift(now.getDate());
      setDate(copyDate);

      let copyHours = [...hours];
      copyHours.unshift(now.getHours());
      setHours(copyHours);

      let copyMinutes = [...minutes];
      copyMinutes.unshift(now.getMinutes());
      setMinutes(copyMinutes);

      document.querySelector("input").value = "";
    }
  };

  return (
    <div className="App">
      <div className="black-nav">
        <h4>ReactBlog</h4>
      </div>
      {/* 가나다순정렬 버튼 누르면 게시글 가나다순 정렬 */}
      <button onClick={sortList}>가나다순정렬</button>

      {/* 게시글 */}
      {title.map((arr, idx) => {
        return (
          <div className="list" key={idx}>
            <h4
              onClick={() => {
                showModal(idx);
              }}
            >
              {title[idx]}
              <span
                onClick={(event) => {
                  incrementLike(idx, event);
                }}
              >
                👍
              </span>
              {like[idx]}
            </h4>
            <p>{`${year[idx]}년 ${month[idx]}월 ${date[idx]}일 ${hours[idx]}시 ${minutes[idx]}분`}</p>
            <button
              onClick={() => {
                deleteArticle(idx);
              }}
            >
              삭제
            </button>
          </div>
        );
      })}
      {modal ? (
        <Modal
          title={title}
          titleIdx={titleIdx}
          year={year}
          month={month}
          date={date}
          hours={hours}
          minutes={minutes}
        />
      ) : null}
      <input
        onChange={(event) => {
          createUserInput(event);
        }}
      ></input>
      <button onClick={createArticle}>생성</button>
    </div>
  );
}

function Modal(props) {
  return (
    <div className="modal">
      <h4>{props.title[props.titleIdx]}</h4>
      <p>{`${props.year[props.titleIdx]}년 ${props.month[props.titleIdx]}월 ${
        props.date[props.titleIdx]
      }일 ${props.hours[props.titleIdx]}시 ${
        props.minutes[props.titleIdx]
      }분`}</p>
      <p>상세내용</p>
      <button>글수정</button>
    </div>
  );
}

export default App;
