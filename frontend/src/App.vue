<script setup>
import { onMounted, ref } from 'vue'
import { getHealth } from './api'

const loading = ref(false)
const connected = ref(false)
const error = ref('')

async function checkConnection() {
  loading.value = true
  connected.value = false
  error.value = ''
  try {
    await getHealth()
    connected.value = true
  } catch {
    error.value = 'API недоступен. Проверьте, что сервер запущен на порту 8000.'
  } finally {
    loading.value = false
  }
}

onMounted(checkConnection)
</script>

<template>
  <main class="card">
    <p class="eyebrow">FASTAPI + VUE</p>
    <h1>Life Stats</h1>
    <p class="description">Каркас приложения готов. Здесь будут ваши данные и статистика.</p>
    <div class="status" role="status" aria-live="polite">
      <span v-if="loading">Проверяем соединение с API…</span>
      <span v-else-if="connected" class="success">● API подключён</span>
      <span v-else class="error">{{ error }}</span>
    </div>
    <button :disabled="loading" @click="checkConnection">
      {{ loading ? 'Проверка…' : 'Проверить соединение' }}
    </button>
  </main>
</template>
