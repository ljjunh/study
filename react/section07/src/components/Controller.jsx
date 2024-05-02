import { useState } from "react";

const Controller = (props) => {
  const [buttonValue, setButtonValue] = useState([-1, -10, -100, 100, 10, 1]);
  return (
    <div>
      {buttonValue.map((item, idx) => {
        return (
          <button
            onClick={() => {
              props.onClickButton(item);
            }}
            key={idx}
          >
            {item}
          </button>
        );
      })}
      {/* <button
        onClick={() => {
          props.onClickButton(-1);
        }}
      >
        -1
      </button>
      <button
        onClick={() => {
          props.onClickButton(-10);
        }}
      >
        -10
      </button>
      <button
        onClick={() => {
          props.onClickButton(-100);
        }}
      >
        -100
      </button>
      <button
        onClick={() => {
          props.onClickButton(100);
        }}
      >
        +100
      </button>
      <button
        onClick={() => {
          props.onClickButton(10);
        }}
      >
        +10
      </button>
      <button
        onClick={() => {
          props.onClickButton(1);
        }}
      >
        +1
      </button> */}
    </div>
  );
};
export default Controller;
