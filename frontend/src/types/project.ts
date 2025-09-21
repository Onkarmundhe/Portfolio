export interface Project {
  id: number
  title: string
  description: string
  image: string
  technologies: string[]
  githubUrl?: string
  liveUrl?: string
  featured: boolean
}

export interface ContactForm {
  name: string
  email: string
  subject: string
  message: string
}
