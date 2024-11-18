import type { AxiosInstance } from "axios";

import type { registrationInfo } from "@/stores/userRegistration";

export async function requestVerificationCode(
  requestBase: AxiosInstance,
  store: registrationInfo
) {
  const resp = await requestBase.post(
    "/mail/send_verification_code?email=" + store.email
  );
  return resp;
}

export async function sendUserInfo(
  requestBase: AxiosInstance,
  store: registrationInfo
) {
  const userInfo: Object = {
    role: store.role,
    name: store.username,
    surname: store.surname,
    email: store.email,
    password: store.password,
    verification_code: store.enteredCode,
  };
  const resp = await requestBase.post("/users/register", userInfo);
  console.log(resp);
  return resp;
}

export async function sendAuthInfo(
  requestBase: AxiosInstance,
  email: string,
  password: string
) {
  const userInfo: Object = {
    email: email,
    password: password,
  };
  const resp = await requestBase.post("/users/login", userInfo);
  console.log(resp);
  return resp;
}
export default function (instance: AxiosInstance) {
  return {
    // async getProfile() {
    //   const response = await instance.get("profile");
    //   return response.data;
    // },
    // async getChats() {
    //   const response = await instance.get("chats");
    //   return response.data;
    // },
    // async getChatData(contact_id) {
    //   const response = await instance.get("chat/messages/" + contact_id);
    //   return response.data.conversation;
    // },
    // async sendMessageToServer(message) {
    //   const axiosConfig = {
    //     headers: {
    //       "Content-Type": "application/json; charset=utf-8",
    //       "Access-Control-Allow-Origin": "*",
    //     },
    //   };
    //   const response = await instance.post(
    //     "/chat/message/send/",
    //     message,
    //     axiosConfig
    //   );
    //   return response.data.conversation;
    // },
    // const axiosConfig = {
    //   headers: {
    //     "Content-Type": "application/json; charset=utf-8",
    //     "Access-Control-Allow-Origin": "*",
    //   },
    // };
  };
}
