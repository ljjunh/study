import { Col } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
const Card = (props) => {
  let navigate = useNavigate();
  return (
    <Col md={4}>
      <img
        src={`https://codingapple1.github.io/shop/shoes${props.idx + 1}.jpg`}
        width="80%"
        onClick={() => {
          navigate(`/detail/${props.idx}`);
        }}
      />
      <h4>{props.arr.title}</h4>
      <p>{props.arr.content}</p>
    </Col>
  );
};
export default Card;
