import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

let DEV_CONFIG = {
  root: "src",
  envDir: "../",
  plugins: [react()],
  server: {
    host: true,
    // Used when running in docker on WSL2
    watch: {
      usePolling: true
    }
  }
}

export default defineConfig(({ command, mode }) => {
  if (mode === 'dev') {
    console.log("Running in development mode")
    return DEV_CONFIG
  } else {
    console.log("Running in production mode")
    return {
      root: "src",
      envDir: "../",
      plugins: [react()]
    }
  }
});