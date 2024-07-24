import React from "react";
import { Routes, Route } from "react-router-dom";
import { SearchBar } from "./components/SearchBar";
import { SearchResult } from "./components/SearchResult";
import { SearchResultDetail } from "./components/SearchResultDetail";
const App: React.FC = () => {
  return (
    <Routes>
      <Route path="/" element={<SearchBar />} />
      <Route path="/search" element={<SearchResult />} />
      <Route path="/video/:videoId" element={<SearchResultDetail />} />
    </Routes>
  );
};

export default App;
