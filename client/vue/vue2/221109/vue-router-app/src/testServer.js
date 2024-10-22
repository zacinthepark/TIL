const express = require('express');
const multer = require('multer');
const cors = require('cors');
const path = require('path');
const fs = require('fs');  // 파일 시스템 모듈 추가
const app = express();

// CORS 미들웨어
app.use(cors());

// Multer 설정: 업로드 디렉토리 설정
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const uploadPath = './uploads';

    // 업로드 디렉토리가 존재하지 않으면 생성
    if (!fs.existsSync(uploadPath)) {
      fs.mkdirSync(uploadPath);
    }

    cb(null, uploadPath);  // 파일을 저장할 폴더 설정
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + path.extname(file.originalname));  // 파일명에 타임스탬프 추가
  }
});

const upload = multer({ storage: storage });

// 파일 업로드 엔드포인트
app.post('/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded.');
  }
  res.send(`File uploaded successfully: ${req.file.filename}`);
});

// 기본 루트
app.get('/', (req, res) => {
  res.send('파일 업로드 서버가 작동 중입니다!');
});

// 서버 실행
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
