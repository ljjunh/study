import React from "react";
import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import { useLocation, Link, useNavigate } from "react-router-dom";
import styled from "styled-components";
const API_KEY = "바꿔쓰셈";
const BASE_URL = "https://www.googleapis.com/youtube/v3/search";

interface YouTubeItem {
  id: {
    kind: string;
    videoId: string;
  };
  snippet: {
    title: string;
    thumbnails: {
      high: {
        url: string;
      };
    };
  };
}

const fetchVideos = async (query: string): Promise<YouTubeItem[]> => {
  try {
    const { data } = await axios.get(BASE_URL, {
      params: {
        part: "snippet",
        q: `${query} #shorts`,
        type: "video",
        videoDuration: "short",
        maxResults: 50,
        key: API_KEY,
      },
    });
    return data.items;
  } catch (error) {
    console.error("Error fetching videos:", error);
    throw error;
  }
};

export const SearchResult: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();
  // URL에서 q의 파라미터 값 가져오기 혹시 모르니까 없을땐 빈문자열
  const query = new URLSearchParams(location.search).get("q") || "";

  const {
    data: videos,
    isLoading,
    isError,
    error,
  } = useQuery({
    queryKey: ["videos", query],
    queryFn: () => fetchVideos(query),
    enabled: !!query,
  });

  const handleVideoClick = (videoId: string) => {
    navigate(`/video/${videoId}?q=${encodeURIComponent(query)}`);
  };

  if (!query)
    return (
      <div>
        검색어가 없습니다. <Link to="/">검색 페이지로 돌아가기</Link>
      </div>
    );
  if (isLoading) return <div>로딩 중...</div>;
  if (isError)
    return (
      <div>
        에러가 발생했습니다: {(error as Error).message}.{" "}
        <Link to="/">다시 검색하기</Link>
      </div>
    );

  return (
    <div>
      <h2>검색 결과: {query}</h2>
      <Link to="/">새로운 검색하기</Link>
      <div
        style={{ display: "flex", flexWrap: "wrap", justifyContent: "center" }}
      >
        {videos && videos.length > 0 ? (
          videos.map((video) => (
            <ThumbnailContainer
              key={video.id.videoId}
              onClick={() => handleVideoClick(video.id.videoId)}
            >
              <ThumbnailImage
                src={video.snippet.thumbnails.high.url}
                alt={video.snippet.title}
              />
              <VideoTitle>{video.snippet.title}</VideoTitle>
            </ThumbnailContainer>
          ))
        ) : (
          <div>검색 결과가 없습니다.</div>
        )}
      </div>
    </div>
  );
};

const ThumbnailContainer = styled.div`
  width: 180px; // 썸네일의 너비를 지정
  aspect-ratio: 9 / 16; // 9:16 비율 설정
  overflow: hidden;
  position: relative;
  margin: 10px;
  cursor: pointer;
`;

const ThumbnailImage = styled.img`
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;
`;

const VideoTitle = styled.p`
  margin-top: 5px;
  font-size: 14px;
  text-align: center;
`;
