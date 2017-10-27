require 'erb'
require 'yaml'

courses_it = { id: "it", title: "資訊科技", courses: [] }
courses_business = { id: "business", title: "商管經濟", courses: []}
courses_asia = { id: "asia", title: "認識亞太", courses: []}
courses_culture = { id: "culture", title: "人文史地", courses: []}

course_hashes = YAML.load(File.open("output.yml").read)

course_hashes.each do |course|
  case course["category"]
    when "資訊科技"
      courses_it[:courses] << course
    when "商管經濟"
      courses_business[:courses] << course
    when "認識亞洲"
      courses_asia[:courses] << course
    when "人文史地"
      courses_culture[:courses] << course
  end
end

@courses = [courses_it, courses_business, courses_asia, courses_culture]

erb = ERB.new(File.open("#{__dir__}/thai.html.erb").read)

output = File.open("#{__dir__}/index.html", "w")
output << erb.result
output.close
