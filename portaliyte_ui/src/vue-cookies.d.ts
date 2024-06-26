// src/vue-cookies.d.ts
declare module 'vue-cookies' {
    interface VueCookies {
      get(key: string): any;
      set(key: string, value: any, options?: any): void;
      remove(key: string): void;
      keys(): string[];
    }
  
    const VueCookies: VueCookies;
    export default VueCookies;
  }
  