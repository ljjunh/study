import "./App.css";
import { useState } from "react";
import Counter from "./components/Counter";
import Bulb from "./components/Bulb";

function App() {
  return (
    <>
      <Bulb />
      <Counter />
    </>
  );
}

export default App;
