import { useParams, useSearchParams } from "react-router-dom";
import { useEffect, useState, useContext } from "react";
import { Nav } from "react-bootstrap";
import { Context1 } from "../App";
import { addItem } from "../store";
import { useDispatch } from "react-redux";
const Detail = (props) => {
  const [tab, setTab] = useState(0);
  const { stock } = useContext(Context1);
  const dispatch = useDispatch();
  useEffect(() => {
    const a = setTimeout(() => {
      setAlert(false);
    }, 2000);
    return () => {
      clearTimeout(a);
    };
  }, []);

  // // useEffect
  // useEffect(()=>{}) 재렌더링마다 코드를 실행하고싶으면
  // useEffect(()=>{},[]) mount시 1회만 실행하고 싶으면
  // useEffect(()=>{
  //   return ()=>{
  //     3. unmount시 1회 코드 실행하고싶으면(cleanup)
  //   }
  // }, [])

  const params = useParams();
  const shoes = props.shoes.find(
    (item) => Number(item.id) === Number(params.id)
  );
  const [count, setCount] = useState(0);
  const [alert, setAlert] = useState(true);
  return (
    <div className="container">
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
      <div className="row">
        <div className="col-md-6">
          <img
            src={`https://codingapple1.github.io/shop/shoes${
              Number(shoes.id) + 1
            }.jpg`}
            width="100%"
          />
        </div>
        <div className="col-md-6">
          <h4 className="pt-5">{shoes.title}</h4>
          <p>{shoes.content}</p>
          <p>{shoes.price}</p>
          <button
            className="btn btn-danger"
            onClick={() => {
              dispatch(addItem({ id: 1, name: "Red Knit", count: 1 }));
            }}
          >
            주문하기
          </button>
        </div>
      </div>
      <Nav variant="tabs" defaultActiveKey="link0">
        <Nav.Item>
          <Nav.Link eventKey="link0" onClick={() => setTab(0)}>
            버튼0
          </Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link eventKey="link1" onClick={() => setTab(1)}>
            버튼1
          </Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link eventKey="link2" onClick={() => setTab(2)}>
            버튼2
          </Nav.Link>
        </Nav.Item>
      </Nav>
      {tab === 0 && <div>{stock}</div>}
      {tab === 1 && <div>내용1</div>}
      {tab === 2 && <div>내용2</div>}
    </div>
  );
};
export default Detail;
