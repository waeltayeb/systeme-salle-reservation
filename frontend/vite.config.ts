import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  preview: {
    host: true,
    port: 4173,
    allowedHosts: ['frontend.local']
  },
  server: {
    proxy: {
      '/users': 'http://api.local',
      '/salles': 'http://api.local',
      '/reservations': 'http://api.local'
    }
  },

  plugins: [react()],
})
