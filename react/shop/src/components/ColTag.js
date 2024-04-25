import { Col } from "react-bootstrap";
const ColTag = (props) => {
  return (
    <Col md={4}>
      <img
        src={`https://codingapple1.github.io/shop/shoes${props.idx + 1}.jpg`}
        width="80%"
      />
      <h4>{props.shoes[props.idx].title}</h4>
      <p>{props.shoes[props.idx].content}</p>
    </Col>
  );
};
export default ColTag;
