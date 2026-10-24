export async function getHealth() {
  const response = await fetch('/api/health', {
    signal: AbortSignal.timeout(5000),
  })
  if (!response.ok) {
    throw new Error(`API вернул ошибку ${response.status}`)
  }
  const data = await response.json()
  if (data.status !== 'ok') {
    throw new Error('Неожиданный ответ API')
  }
  return data
}
