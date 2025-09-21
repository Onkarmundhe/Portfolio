import Head from 'next/head'
import Layout from '../components/Layout'
import Hero from '../components/Hero'
import About from '../components/About'
import Projects from '../components/Projects'
import Contact from '../components/Contact'
import Skills from '../components/Skills'
import Chatbot from '../components/Chatbot'

export default function Home() {
  // Static projects data - no need for API calls
  const projects = [
    {
      id: 1,
      title: "E-Commerce Platform",
      description: "A full-stack e-commerce solution built with React, Node.js, and PostgreSQL. Features include user authentication, product management, shopping cart, and payment integration.",
      image: "https://via.placeholder.com/600x400/4F46E5/FFFFFF?text=E-Commerce+Platform",
      technologies: ["React", "Node.js", "PostgreSQL", "Stripe", "Tailwind CSS"],
      githubUrl: "https://github.com/onkarmundhe/ecommerce-platform",
      liveUrl: "https://ecommerce-demo.com",
      featured: true
    },
    {
      id: 2,
      title: "Task Management App",
      description: "A collaborative task management application with real-time updates, drag-and-drop functionality, and team collaboration features.",
      image: "https://via.placeholder.com/600x400/7C3AED/FFFFFF?text=Task+Management+App",
      technologies: ["Next.js", "TypeScript", "Socket.io", "MongoDB", "Prisma"],
      githubUrl: "https://github.com/onkarmundhe/task-manager",
      liveUrl: "https://taskmanager-demo.com",
      featured: true
    },
    {
      id: 3,
      title: "Weather Dashboard",
      description: "A responsive weather dashboard that displays current weather conditions and forecasts using data from multiple weather APIs.",
      image: "https://via.placeholder.com/600x400/059669/FFFFFF?text=Weather+Dashboard",
      technologies: ["React", "Chart.js", "OpenWeather API", "CSS3"],
      githubUrl: "https://github.com/onkarmundhe/weather-dashboard",
      liveUrl: "https://weather-demo.com",
      featured: false
    },
    {
      id: 4,
      title: "Portfolio Website",
      description: "A modern, responsive portfolio website built with Next.js and FastAPI, featuring dynamic content management and contact form integration.",
      image: "https://via.placeholder.com/600x400/DC2626/FFFFFF?text=Portfolio+Website",
      technologies: ["Next.js", "TypeScript", "FastAPI", "Python", "Tailwind CSS"],
      githubUrl: "https://github.com/onkarmundhe/portfolio",
      liveUrl: "https://onkarmundhe.dev",
      featured: true
    }
  ]

  return (
    <Layout>
      <Head>
        <title>Onkar Mundhe - Software Development Engineer</title>
        <meta name="description" content="Portfolio of Onkar Mundhe - Software Development Engineer" />
      </Head>
      
      <Hero />
      <About />
      <Skills />
      <Projects projects={projects} />
      <Contact />
      <Chatbot />
    </Layout>
  )
}
