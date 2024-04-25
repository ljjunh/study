import { Col } from "react-bootstrap";
const Card = (props) => {
  return (
    <Col md={4}>
      <img
        src={`https://codingapple1.github.io/shop/shoes${props.idx + 1}.jpg`}
        width="80%"
      />
      <h4>{props.arr.title}</h4>
      <p>{props.arr.content}</p>
    </Col>
  );
};
export default Card;
