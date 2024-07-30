import React from "react";
import { Routes, Route } from "react-router-dom";
import { SearchBar } from "./components/SearchBar";
import { SearchResult } from "./components/SearchResult";
import { SearchResultDetail } from "./components/SearchResultDetail";
import { WebcamRecorder } from "./components/WebcamRecorder";
import { Practice } from "./components/Practice";
import PoseLandmarkerComponent from "./components/PoseLandmarkerComponent";
const App: React.FC = () => {
  return (
    <Routes>
      <Route path="/" element={<SearchBar />} />
      <Route path="/search" element={<SearchResult />} />
      <Route path="/video/:videoId" element={<SearchResultDetail />} />
      <Route path="/webCam" element={<WebcamRecorder />} />
      <Route path="/practice/:videoId" element={<Practice />} />
      <Route path="/pose" element={<PoseLandmarkerComponent />} />
    </Routes>
  );
};

export default App;
