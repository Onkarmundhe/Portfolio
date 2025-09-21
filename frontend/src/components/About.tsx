export default function About() {
  return (
    <section id="about" className="py-20 bg-white dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            About Me
          </h2>
          <div className="w-24 h-1 bg-gradient-to-r from-blue-600 to-purple-600 mx-auto"></div>
        </div>
        
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div className="space-y-6">
            <div className="text-lg text-gray-600 dark:text-gray-300 leading-relaxed">
              <p className="mb-4">
                I'm a passionate Software Development Engineer with a strong foundation in 
                full-stack development. I love creating efficient, scalable, and user-friendly 
                applications that solve real-world problems.
              </p>
              <p className="mb-4">
                With expertise in modern web technologies and frameworks, I enjoy working on 
                challenging projects that push the boundaries of what's possible. I'm always 
                eager to learn new technologies and stay up-to-date with industry best practices.
              </p>
              <p>
                When I'm not coding, you can find me exploring new technologies, contributing 
                to open-source projects, or sharing knowledge with the developer community.
              </p>
            </div>
            
            <div className="flex flex-wrap gap-4">
              <div className="bg-blue-50 dark:bg-blue-900/20 px-4 py-2 rounded-full">
                <span className="text-blue-700 dark:text-blue-300 font-medium">Problem Solver</span>
              </div>
              <div className="bg-purple-50 dark:bg-purple-900/20 px-4 py-2 rounded-full">
                <span className="text-purple-700 dark:text-purple-300 font-medium">Team Player</span>
              </div>
              <div className="bg-green-50 dark:bg-green-900/20 px-4 py-2 rounded-full">
                <span className="text-green-700 dark:text-green-300 font-medium">Continuous Learner</span>
              </div>
            </div>
          </div>
          
          <div className="relative">
            <div className="bg-gradient-to-br from-blue-600 to-purple-600 rounded-lg p-8 text-white">
              <h3 className="text-2xl font-bold mb-4">My Journey</h3>
              <div className="space-y-4">
                <div className="flex items-start space-x-3">
                  <div className="w-2 h-2 bg-white rounded-full mt-2 flex-shrink-0"></div>
                  <div>
                    <h4 className="font-semibold">Software Development Engineer</h4>
                    <p className="text-blue-100 text-sm">Building scalable web applications</p>
                  </div>
                </div>
                <div className="flex items-start space-x-3">
                  <div className="w-2 h-2 bg-white rounded-full mt-2 flex-shrink-0"></div>
                  <div>
                    <h4 className="font-semibold">Full-Stack Development</h4>
                    <p className="text-blue-100 text-sm">Frontend and backend expertise</p>
                  </div>
                </div>
                <div className="flex items-start space-x-3">
                  <div className="w-2 h-2 bg-white rounded-full mt-2 flex-shrink-0"></div>
                  <div>
                    <h4 className="font-semibold">Technology Enthusiast</h4>
                    <p className="text-blue-100 text-sm">Always exploring new technologies</p>
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
