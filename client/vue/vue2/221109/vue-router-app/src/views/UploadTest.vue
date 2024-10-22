<template>
  <div class="upload-container">
    <!-- 드래그앤드랍 영역 -->
    <div class="drag-drop-area" 
        @drop.prevent="handleDrop" 
        @dragover.prevent>
      <!-- 파일이 하나도 없을 때 표시되는 문구 -->
      <p v-if="!files.length" class="placeholder-text">Drag&Drop으로 사진 및 PDF 파일 업로드</p>
      
      <!-- 업로드된 파일 목록 -->
      <div v-if="files.length" class="file-preview-list">
        <div class="file-preview-item" v-for="(file, index) in files" :key="index">
          <!-- 이미지 미리보기 -->
          <img v-if="file.isImage" :src="file.preview" alt="미리보기 이미지" class="preview-img"/>
          <!-- PDF 파일은 미리보기를 제공하지 않고 파일 이름만 표시 -->
          <span v-if="file.isPDF" class="pdf-icon">📄</span>
          <span class="file-name">{{ file.name }}</span>
          <button @click.stop="removeFile(index)">삭제</button>
        </div>
      </div>
    </div>
    
    <!-- 버튼들 -->
    <div class="buttons">
      <button @click="triggerFileInput">파일 업로드</button>
      <button @click="resetUploads" :disabled="!files.length">업로드 초기화</button>
      <button @click="startUpload" :disabled="!files.length">업로드 시작</button>
    </div>

    <!-- 숨겨진 파일 입력 -->
    <input type="file" ref="fileInput" @change="handleFileChange" multiple hidden>

    <!-- 모달 창 -->
    <div v-if="showModal" class="modal-overlay">
      <div class="modal">
        <button class="close-btn" @click="closeModal">X</button>
        <ul>
          <li v-for="(file, index) in files" :key="index" class="file-list-item">
            <span>{{ file.name }} - {{ file.uploadStatus === 'completed' ? '완료' : file.uploadStatus === 'failed' ? '실패' : file.uploadProgress + '%' }}</span>
            <div class="progress-bar">
              <div class="progress" :style="{ width: file.uploadProgress + '%' }"></div>
            </div>
            <button v-if="file.uploadStatus === 'failed'" @click="retryUpload(index)" class="retry-btn">재시도</button>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
const testURL = 'https://c4e4e280-d2d6-40bc-989b-c4b2244b74f6-00-bghvt9q24y4w.janeway.replit.dev/upload'

export default {
  data() {
    return {
      files: [],  // 업로드할 파일 목록
      showModal: false,  // 모달 창 표시 여부
    };
  },
  methods: {
    triggerFileInput() {
      this.$refs.fileInput.click();
    },
    handleFileChange(event) {
      for (const file of event.target.files) {
        this.addFile(file);
      }
    },
    handleDrop(event) {
      for (const file of event.dataTransfer.files) {
        this.addFile(file);
      }
    },
    addFile(file) {
      const reader = new FileReader();
      const fileExtension = file.name.split('.').pop().toLowerCase();
      const isImage = ['jpg', 'jpeg', 'png', 'gif'].includes(fileExtension);
      const isPDF = fileExtension === 'pdf';

      if (isImage) {
        reader.onload = (e) => {
          this.files.push({
            file,
            name: file.name,
            preview: e.target.result,  // 미리보기 이미지 저장
            isImage: true,
            isPDF: false,
            uploadProgress: 0,
            uploadStatus: 'pending'
          });
        };
        reader.readAsDataURL(file);  // 파일을 Base64로 변환하여 미리보기 이미지 생성
      } else if (isPDF) {
        this.files.push({
          file,
          name: file.name,
          preview: null,  // PDF는 미리보기가 없으므로 null
          isImage: false,
          isPDF: true,
          uploadProgress: 0,
          uploadStatus: 'pending'
        });
      }
    },
    removeFile(index) {
      this.files.splice(index, 1);
    },
    resetUploads() {
      this.files = [];  // 업로드한 파일 모두 제거
    },
    startUpload() {
      this.showModal = true;  // 모달 창을 띄움
      this.files.forEach((file, index) => {
        this.uploadFile(file, index);
      });
    },
    async uploadFile(fileWrapper, index) {
      const formData = new FormData();
      formData.append('file', fileWrapper.file);

      try {
        await axios.post(testURL, formData, {
          onUploadProgress: (progressEvent) => {
            const progress = Math.round((progressEvent.loaded * 100) / progressEvent.total);
            this.$set(this.files[index], 'uploadProgress', progress);
          }
        });

        this.$set(this.files[index], 'uploadStatus', 'completed');
      } catch (error) {
        this.$set(this.files[index], 'uploadStatus', 'failed');
      }
    },
    retryUpload(index) {
      this.$set(this.files[index], 'uploadProgress', 0);
      this.$set(this.files[index], 'uploadStatus', 'pending');
      this.uploadFile(this.files[index], index);
    },
    closeModal() {
      // 모달을 닫을 때 업로드 완료된 파일들을 제거
      this.files = this.files.filter(file => file.uploadStatus !== 'completed');
      this.showModal = false;
    }
  }
};
</script>

<style>
.upload-container {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  padding: 20px;
  border: 1px solid #ccc;
  position: relative;
  max-width: 100%;
}

.drag-drop-area {
  width: 100%;
  height: 450px;
  border: 2px dashed #ccc;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  cursor: pointer;
  overflow-y: auto;  /* 스크롤을 추가 */
}

.placeholder-text {
  color: #999;
  font-size: 16px;
  text-align: center;
}

.file-preview-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));  /* 반응형 그리드 */
  gap: 10px;
  padding: 10px;
  width: 100%;
  box-sizing: border-box;
  max-height: 300px;
  overflow-y: auto;  /* 파일 목록에 스크롤 추가 */
}

.file-preview-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.preview-img {
  width: 100%;
  height: auto;
  max-width: 80px;
  max-height: 80px;
  object-fit: cover;
  margin-bottom: 5px;
}

.pdf-icon {
  font-size: 40px;
  margin-bottom: 5px;
}

.file-name {
  width: 80px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;  /* 파일명이 영역을 벗어나면 '...'로 처리 */
  margin-bottom: 5px;
}

.buttons {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 10px;
}

.buttons button {
  padding: 10px 15px;
  border: none;
  cursor: pointer;
  background-color: #007bff;
  color: white;
  border-radius: 5px;
}

.buttons button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

/* 모달 창 배경 불투명 처리 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* 반투명 */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

/* 모달 창 스타일 */
.modal {
  background-color: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  max-width: 600px;
  width: 100%;
  position: relative;
}

/* 모달 닫기 버튼 */
.close-btn {
  position: absolute;
  top: 15px;
  right: 15px;
  background: none;
  border: none;
  font-size: 24px;
  font-weight: bold;
  color: #333;
  cursor: pointer;
  transition: transform 0.2s, color 0.2s;
}

.close-btn:hover {
  transform: scale(1.4); /* 크기 확실하게 커짐 */
  color: #ff6347;
}

/* 파일 정보 스타일 */
.file-list-item {
  list-style-type: none;
  margin-bottom: 20px; /* 파일 정보 간격 추가 */
}

/* 프로그래스 바 스타일 */
.progress-bar {
  width: 100%;
  height: 10px;
  background-color: #e0e0e0;
  border-radius: 5px;
  margin-top: 10px; /* 리스트 bullet과의 간격 조정 */
  overflow: hidden;
}

.progress {
  height: 100%;
  background-color: #007bff;
}

/* 재시도 버튼 스타일 */
.retry-btn {
  margin-top: 5px;
  padding: 5px 10px;
  background-color: #ff6347;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.retry-btn:hover {
  background-color: #ff4500;
}

@media (max-width: 600px) {
  .modal {
    max-width: 90%;
    padding: 20px;
  }
  .drag-drop-area {
    height: auto;
  }

  .file-preview-item {
    max-width: 100px;
  }

  .preview-img {
    max-width: 60px;
    max-height: 60px;
  }

  .file-name {
    width: 60px;
  }

  .buttons {
    flex-direction: column;
  }
}
</style>
