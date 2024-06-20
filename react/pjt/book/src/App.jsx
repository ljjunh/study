import "./App.css";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Report from "./pages/Report";
import BookRecommendation from "./pages/BookRecommendation";

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/report" element={<Report />}></Route>
        <Route
          path="/bookRecommendation"
          element={<BookRecommendation />}
        ></Route>
      </Routes>
    </>
  );
}

export default App;
