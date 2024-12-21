<script setup lang="ts">
import Button from "primevue/button";
import FileUpload from "primevue/fileupload";
import Badge from "primevue/badge";
import OverlayBadge from "primevue/overlaybadge";
import { ref } from "vue";
import { usePrimeVue } from "primevue/config";
import { useToast } from "primevue/usetoast";
const toast = useToast();
const fileupload = ref();

const upload = () => {
  fileupload.value.upload();
};

const onUpload = () => {
  toast.add({
    severity: "info",
    summary: "Success",
    detail: "File Uploaded",
    life: 3000,
  });
};

const $primevue = usePrimeVue();

const totalSize = ref(0);
const totalSizePercent = ref(0);
const files = ref([]);

const onRemoveTemplatingFile = (file: File, removeFileCallback, index) => {
  removeFileCallback(index);
  totalSize.value -= parseInt(formatSize(file.size));
  totalSizePercent.value = totalSize.value / 10;
};

const onClearTemplatingUpload = (clear) => {
  clear();
  totalSize.value = 0;
  totalSizePercent.value = 0;
};

const onSelectedFiles = (event: Event) => {
  files.value = event.files;
  files.value.forEach((file) => {
    totalSize.value += parseInt(formatSize(file.size));
  });
};

const uploadEvent = (callback) => {
  totalSizePercent.value = totalSize.value / 10;
  callback();
};

const onTemplatedUpload = () => {
  toast.add({
    severity: "info",
    summary: "Success",
    detail: "File Uploaded",
    life: 3000,
  });
};

const formatSize = (bytes) => {
  const k = 1024;
  const dm = 3;
  const sizes = $primevue.config.locale.fileSizeTypes;

  if (bytes === 0) {
    return `0 ${sizes[0]}`;
  }

  const i = Math.floor(Math.log(bytes) / Math.log(k));
  const formattedSize = parseFloat((bytes / Math.pow(k, i)).toFixed(dm));

  return `${formattedSize} ${sizes[i]}`;
};
</script>
<template>
  <section class="loader">
    <div class="loader-container">
      <Toast />
      <FileUpload
        ref="fileupload"
        mode="advanced"
        name="demo[]"
        url="/api/upload"
        chooseLabel="выбрать файлы"
        uploadLabel="загрузить"
        cancelLabel="отменить"
        :multiple="true"
        :dragDropSupport="true"
        @upload="onUpload"
      >
        <template #empty>
          <p class="loader-description">
            Перетащите ваши файлы или нажмите на кнопку для выбора файлов
          </p>
        </template>
        <template
          #content="{
            files,
            uploadedFiles,
            removeUploadedFileCallback,
            removeFileCallback,
          }"
        >
          <div>
            <div v-if="files.length > 0" style="display: flex; gap: 0 20px">
              <div
                style="
                  display: flex;
                  flex-wrap: wrap;
                  gap: 10px 20px;
                  justify-content: center;
                "
              >
                <div
                  v-for="(file, index) of files"
                  :key="file.name + file.type + file.size"
                  style="
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                    align-items: center;
                    gap: 10px;
                    max-width: 200px;
                    width: 100%;
                    padding: 25px;
                    border-radius: 10px;
                    background-color: #444;
                  "
                >
                  <div>
                    <img
                      v-if="file.objectURL"
                      role="presentation"
                      :alt="file.name"
                      :src="file.objectURL"
                      style="
                        white-space: nowrap;
                        overflow: hidden;
                        text-overflow: ellipsis;
                        text-align: center;
                        width: 150px;
                        height: 100px;
                        object-fit: cover;
                      "
                    />
                  </div>
                  <span
                    style="
                      width: 100%;
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                      text-align: center;
                    "
                    >{{ file.name }}</span
                  >
                  <div style="text-align: center">
                    {{ formatSize(file.size) }}
                  </div>
                  <Badge value="Ожидает отправки" severity="warn" />
                  <Button
                    icon="pi pi-times"
                    @click="
                      onRemoveTemplatingFile(file, removeFileCallback, index)
                    "
                    outlined
                    rounded
                    severity="danger"
                  />
                </div>
              </div>
            </div>
          </div>
        </template>
      </FileUpload>
    </div>
  </section>
</template>
<style scoped>
.loader {
  animation: animate 1s infinite;
}

.loader {
  /* border-style: ; */

  border-radius: 20px;
}
.loader-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.loader-description {
  text-align: center;
  font-size: 1rem;
  font-weight: 200;
  color: #696868;
}
/* Style the upload area */

:deep(.p-fileupload) {
  width: 100%;
  background-color: #444;
  border: none;
}

/* Add smooth transitions */
:deep(.p-fileupload *) {
  transition: all 0.3s ease;
}

/* Add animation for drag state */
@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.02);
  }
  100% {
    transform: scale(1);
  }
}

:deep(.p-fileupload-highlight) {
  animation: pulse 1s infinite;
}

:deep(.p-fileupload-content) {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  min-height: 300px;
  border: 2px dashed #444;
  border-radius: 6px;
  background-color: #333;
  transition: border-color 0.3s;
  transition: background-color 0.5s;
}

:deep(.p-fileupload-content:hover) {
  border-color: var(--p-primary-color);
  /* background-color: #eef2ff; */
}

/* Style the drag-over state */
:deep(.p-fileupload-content.p-fileupload-highlight) {
  border-color: var(--p-primary-color);
  /* background-color: #eef2ff; */
}
</style>
