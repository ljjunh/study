import { Container, Row, Col, Nav } from "react-bootstrap";
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { addItem } from "../store";
const Detail = (props) => {
  //mount, updata시 실행
  // useEffect 안에 있는 코드는 html 렌더링 후에 동작함
  // useEffect에 넣어두면 좋은것들
  // 오래걸리는 작업을 넣어두면 html을 먼저 보여주고 실행해서 좋음
  // 서버에서 데이터 가져오는 작업
  // 타이머 장착하는거
  let dispatch = useDispatch();

  let [count, setCount] = useState(0);

  let { id } = useParams();
  // 유저가 URL파라미터에 입력한거 가져오려면 useParams()
  const imgId = parseInt(id) + 1;
  // 파라미터는 문자열이니까 정수로 변환해주고 쓰기
  const data = props.shoes.find((item) => item.id == id);
  // 변환하기 귀찮아서 문자열인 파라미터와 정수형인 id ==로 비교
  let [alertPage, setAlertPage] = useState(true);
  useEffect(() => {
    const timer = setTimeout(() => {
      setAlertPage(false);
    }, 2000);
    return () => {
      //기존 타이머는 제거
      clearTimeout(timer);
    };
  }, []);

  // useEffect(()=>{}) 1. 재렌더링마다 코드실행하고싶으면
  // useEffect(()=>{}, []) 2. mount시 1회 코드 실행하고싶으면
  // useEffect(()=>{
  //   return ()=>{
  //    3. unmount시 1회 코드실행하고 싶으면
  //   }
  // })
  // useEffect 동작 전에 실행하려면 return()=>{}
  // useEffect(()=>{}, [count]) 5. 특정 state변경시에만 실행하려면 [state명]

  //input에 숫자말고 다른거 입력하면 alert
  const [num, setNum] = useState("");
  useEffect(() => {
    if (isNaN(num) == true) {
      alert("숫자만 입력 가능합니다");
    }
  }, [num]);

  // 탭 만들기
  const [tabState, setTabState] = useState(0);
  // Detail 컴포넌트 등장할때 애니메이션 주기
  const [fade2, setFade2] = useState("");
  useEffect(() => {
    setFade2("end");
    return () => {
      setFade2("");
    };
  }, []);

  // 상세페이지에서 봤던 상품의 id를 localStorage에 저장하기
  useEffect(() => {
    //data.id
    let watchedArr = JSON.parse(localStorage.getItem("watched"));
    //새로운 id 추가
    watchedArr.push(data.id);
    //중복제거
    watchedArr = new Set(watchedArr);
    //다시 arr로 변환
    watchedArr = Array.from(watchedArr);
    //localStorage에 변경된 arr 덮어쓰기
    localStorage.setItem("watched", JSON.stringify(watchedArr));
  }, []);

  return (
    <Container className={`start ${fade2}`}>
      {alertPage ? (
        <div className="alert alert-warning">2초이내 구매시 할인</div>
      ) : null}
      {count}
      <button
        onClick={() => {
          setCount(count + 1);
        }}
      >
        버튼
      </button>
      <Row>
        <Col md={6}>
          <img
            src={`https://codingapple1.github.io/shop/shoes${imgId}.jpg`}
            width="100%"
          />
        </Col>
        <Col md={6}>
          <input
            onChange={(e) => {
              setNum(e.target.value);
            }}
          ></input>
          <h4>{data.title}</h4>
          <p>{data.content}</p>
          <p>{data.price}원</p>
          <button
            className="btn btn-danger"
            onClick={() => {
              dispatch(addItem({ id: data.id, name: data.title, count: 0 }));
            }}
          >
            주문하기
          </button>
        </Col>
      </Row>
      <Nav variant="tabs" defaultActiveKey="link0">
        <Nav.Item>
          <Nav.Link
            onClick={() => {
              setTabState(0);
            }}
            eventKey="link0"
          >
            버튼0
          </Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link
            onClick={() => {
              setTabState(1);
            }}
            eventKey="link1"
          >
            버튼1
          </Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link
            onClick={() => {
              setTabState(2);
            }}
            eventKey="link2"
          >
            버튼2
          </Nav.Link>
        </Nav.Item>
      </Nav>
      <TabContent tabState={tabState} />
    </Container>
  );
};
function TabContent({ tabState }) {
  let [fade, setFade] = useState("");
  useEffect(() => {
    let timer = setTimeout(() => {
      setFade("end");
    }, 100);
    return () => {
      setFade("");
      clearTimeout(timer);
    };
  }, [tabState]);
  return (
    <div className={`start ${fade}`}>
      {[<div>내용0</div>, <div>내용1</div>, <div>내용2</div>][tabState]}
    </div>
  );
}
export default Detail;
