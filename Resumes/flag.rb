## This program flags any resumes that do not contain "and" or "the" and may need to be converted to PNG format
require "pdf-reader"

resumes = Dir["Analytics/Intro to Analytics/MSiA 400 Resumes/Resume Packet NonAnalytics/*/*"]

resumes.each do |r|
  resume = PDF::Reader.new(r)
  text = ""
  resume.pages.each do |pp|
    text = text + " "
    text = text + pp.text
  end
  text.gsub!(",","")
  text.gsub!("(","")
  text.gsub!(")","")
  text.gsub!("[","")
  text.gsub!("]","")
  text.downcase!
  arr = text.split
  if !(arr.include?("and") || arr.include?("the"))
    puts r
  end
end