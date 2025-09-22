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
      title: "Typing Speed Test",
      description: "A modern, responsive typing speed test application that measures typing speed (WPM), accuracy, and streak in real-time. Features adaptive cursor, theme support, and immediate visual feedback for typing mistakes.",
      image: "/images/typing_speed_test.png",
      technologies: ["JavaScript", "HTML", "CSS", "Google Fonts"],
      githubUrl: "https://github.com/Onkarmundhe/typing-speed-test.git",
      liveUrl: "",
      featured: true
    },
    {
      id: 2,
      title: "GitHub Repository Analyzer",
      description: "A Flask-based application that analyzes GitHub repositories using the Gemini 2.0 Flash AI model. Features repository data fetching, code structure analysis, language breakdown statistics, dependency identification, and AI-powered insights.",
      image: "/images/github_analyzer.png",
      technologies: ["Python", "Flask", "Gemini AI", "GitHub API", "RESTful API"],
      githubUrl: "https://github.com/Onkarmundhe/Github_repo_analyzer",
      liveUrl: "",
      featured: true
    },
    {
      id: 3,
      title: "PDF Summary Generator",
      description: "A Streamlit-based web application that generates concise summaries of PDF documents using AI models. Features easy PDF upload interface, text extraction, and both detailed and concise summary generation with a clean, intuitive user interface.",
      image: "/images/pdf_summary_generator.png",
      technologies: ["Python", "Streamlit", "Groq API", "Gemini AI", "PDF Processing"],
      githubUrl: "https://github.com/Onkarmundhe/pdf-summary-generator.git",
      liveUrl: "",
      featured: true
    },
    {
      id: 4,
      title: "Weakly-Hard Real-Time Task Scheduling",
      description: "Implementation of different approaches for scheduling weakly-hard real-time tasks using various patterns and algorithms. Features Integer Linear Programming solution with Gurobi optimizer, E-pattern and R-pattern scheduling implementations with (m,k)-firm guarantees.",
      image: "/images/realtime_scheduling.png",
      technologies: ["Python", "Gurobi Optimizer", "Integer Linear Programming", "Real-Time Systems"],
      githubUrl: "https://github.com/Onkarmundhe/Weakly-Hard-Real-Time-Scheduling",
      liveUrl: "",
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
