import "./Editor.css";
import { useState, useRef } from "react";
const Editor = ({ onCreate }) => {
  return (
    <div className="Editor">
      <input placeholder="새로운 Todo..." />
      <button>추가</button>
    </div>
  );
};
export default Editor;
