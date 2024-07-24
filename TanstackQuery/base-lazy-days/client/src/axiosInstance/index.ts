import axios, { AxiosRequestConfig } from "axios";

import { baseUrl } from "./constants";
import { useEffect } from "react";

// jwt토큰을 받아 인증 헤더 객체 생성
// Record<string,string>은 ts에서 문자열 키와 문자열 값을 가진 객체 타입
export function getJWTHeader(userToken: string): Record<string, string> {
  return { Authorization: `Bearer ${userToken}` };
}

// AxiosRequestConfig 타입을 설정 객체 생성, baseUrl로 모든 요청의 기본 URL 지정
const config: AxiosRequestConfig = { baseURL: baseUrl };
export const axiosInstance = axios.create(config);
// axios.create로 새로운 axios 인스턴스 생성
// 생성된 인스턴스를 axiosInstance로 내보내서 다른파일에서 사용하게 해줌

// 사용 예시
// import {axiosInstance, getJWTHeader} from "..."
// 인증이 필요 없는 요청
// axiosInstance.get('/users');

// JWT 인증이 필요한 요청
// const token = "토큰" 스토어에서 꺼내와서 쓰셈
// axiosInstance.get('/protected-route', {headers:getJWTHeader(token)})
