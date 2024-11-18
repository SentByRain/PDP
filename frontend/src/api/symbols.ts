import type { InjectionKey } from "vue";
import type { AxiosInstance } from "axios";

import type { registrationInfo } from "@/stores/userRegistration";


export const AxiosKey: InjectionKey<AxiosInstance> = Symbol("requestBase");
export const RegStoreKey: InjectionKey<registrationInfo> = Symbol("userRegStore");