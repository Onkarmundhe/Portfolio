export default function About() {
  return (
    <section id="about" className="py-32 min-h-screen bg-gradient-to-br from-gray-50 to-white dark:from-gray-900 dark:to-gray-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            About Me
          </h2>
          <div className="w-24 h-1 bg-gradient-to-r from-blue-600 to-purple-600 mx-auto rounded-full"></div>
        </div>
        
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div className="space-y-8">
            <div className="text-xl lg:text-2xl text-gray-600 dark:text-gray-300 leading-relaxed">
              <p className="mb-6 hover:text-gray-800 dark:hover:text-gray-100 transition-colors duration-300">
                Software Development Engineer (AI/ML) at ProcessVenue with expertise in SaaS development, RAG systems, and multi-agent architectures. Recent BTech graduate in Mathematics and Computing from IIT Goa, passionate about building intelligent solutions and bridging theory with practical software development.
              </p>
            </div>
          </div>
          
          <div className="relative">
            <div className="bg-gradient-to-br from-blue-600 to-purple-600 rounded-lg p-10 lg:p-12 text-white shadow-xl hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 min-h-[400px] lg:min-h-[500px]">
              <h3 className="text-3xl lg:text-4xl font-bold mb-8">My Journey</h3>
              <div className="space-y-8">
                <div className="border-l-4 border-white/30 pl-8 relative hover:border-white/50 transition-colors duration-300">
                  <div className="absolute -left-2 top-0 w-4 h-4 bg-white rounded-full animate-pulse"></div>
                  <div>
                    <h4 className="font-bold text-xl lg:text-2xl mb-2">Software Development Engineer</h4>
                    <p className="text-blue-100 text-base lg:text-lg font-medium mb-2">Jul 2025 - Present</p>
                    <p className="text-blue-50 text-base lg:text-lg">Predusk Technology Private Limited</p>
                  </div>
                </div>
                <div className="border-l-4 border-white/30 pl-8 relative hover:border-white/50 transition-colors duration-300">
                  <div className="absolute -left-2 top-0 w-4 h-4 bg-white/70 rounded-full"></div>
                  <div>
                    <h4 className="font-bold text-xl lg:text-2xl mb-2">Business Analytics and Intelligence</h4>
                    <p className="text-blue-100 text-base lg:text-lg font-medium mb-1">Internship</p>
                    <p className="text-blue-100 text-base lg:text-lg font-medium mb-2">Dec 2024 - Jun 2025</p>
                    <p className="text-blue-50 text-base lg:text-lg">Predusk Technology Private Limited</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
