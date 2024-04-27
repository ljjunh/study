import { Container, Row, Col } from "react-bootstrap";
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";

const Detail = (props) => {
  useEffect(() => {
    console.log("안녕");
  });
  //mount, updata시 실행
  // useEffect 안에 있는 코드는 html 렌더링 후에 동작함
  // useEffect에 넣어두면 좋은것들
  // 오래걸리는 작업을 넣어두면 html을 먼저 보여주고 실행해서 좋음
  // 서버에서 데이터 가져오는 작업
  // 타이머 장착하는거

  let [count, setCount] = useState(0);

  let { id } = useParams();
  // 유저가 URL파라미터에 입력한거 가져오려면 useParams()
  const imgId = parseInt(id) + 1;
  // 파라미터는 문자열이니까 정수로 변환해주고 쓰기
  const data = props.shoes.find((item) => item.id == id);
  // 변환하기 귀찮아서 문자열인 파라미터와 정수형인 id ==로 비교
  let [alert, setAlert] = useState(true);
  useEffect(() => {
    const timer = setTimeout(() => {
      setAlert(false);
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

  //과제!!! input에 숫자만 입력하게만드려고 다른값오면 알려주기
  // 1. 알림창 만들고 state연결하고 false
  // 2. useEffect에 input값 숫자아니면 알림창 뜨도록

  return (
    <Container>
      {alert ? (
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
          <h4>{data.title}</h4>
          <p>{data.content}</p>
          <p>{data.price}원</p>
          <button className="btn btn-danger">주문하기</button>
        </Col>
      </Row>
    </Container>
  );
};
export default Detail;
