import { defineConfig } from 'vite';
import { resolve } from 'path';
import fs from 'fs';

// Lê todos os arquivos HTML da pasta expedicoes
const expedicoesDir = resolve(__dirname, 'expedicoes');
const expedicoesFiles = fs.readdirSync(expedicoesDir).filter(file => file.endsWith('.html'));

// Configura o index.html principal
const inputs = {
  main: resolve(__dirname, 'index.html'),
};

// Adiciona dinamicamente cada página de expedição ao build
expedicoesFiles.forEach(file => {
  const name = file.replace('.html', '');
  inputs[name] = resolve(expedicoesDir, file);
});

export default defineConfig({
  build: {
    rollupOptions: {
      input: inputs
    }
  }
});
