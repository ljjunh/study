import "./App.css";
import Viewer from "./components/Viewer";
import Controller from "./components/Controller";
import { useState, useEffect } from "react";
function App() {
  const [cnt, setCnt] = useState(0);
  const [input, setInput] = useState("");
  useEffect(() => {
    console.log(`cnt:${cnt} / input: ${input}`);
  }, [cnt, input]);

  const onClickButton = (value) => {
    setCnt(cnt + value);
  };
  return (
    <div className="App">
      <h1>Simple Counter</h1>
      <section>
        <input
          value={input}
          onChange={(e) => {
            setInput(e.target.value);
          }}
        ></input>
      </section>
      <section>
        <Viewer cnt={cnt} />
      </section>
      <section>
        <Controller onClickButton={onClickButton} />
      </section>
    </div>
  );
}

export default App;
