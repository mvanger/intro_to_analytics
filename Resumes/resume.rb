# These are Ruby gems. The first allows reading of PDFs, the second is for testing
require "pdf-reader"
require "pry"

# This loads a PDF as a Ruby object
reader = PDF::Reader.new("Documents/Job Search/Michael Vanger Resume.pdf")

# Some resumes may be more than one page
# So just loop through the reader.pages array
text = ""

# This sets text as a string of all the text in a resume
reader.pages.each do |pp|
  text = text + " "
  text = text + pp.text
end

# Replaces , ( ) with empty strings
# What are some other symbols?
# Also stop words
text.gsub!(",","")
text.gsub!("(","")
text.gsub!(")","")
# This ● is throwing an error
# But it works in pry for some reason
# text.gsub!("●","")

# Turns string into an array
# It splits on the spaces (" ")
arr = text.split

# Instantiates an empty hash
# A hash is a key: value pair
# So it will store the keywords and their counts
keywords = {}

# Loops through array
# If keyword is present, adds 1 to the counter
# If not present, instantiates it with a count of 1
arr.each do |word|
  if keywords.has_key?(word)
    keywords[:"#{word}"] = keywords[:"#{word}"] + 1
  else
    keywords[:"#{word}"] = 1
  end
end

# Prints keywords and their count to the screen
keywords.each do |key, value|
  puts "#{key}: #{value}"
end

# My resume, somehow, doesn't use any words twice. Or I have an error somewhere.

# It may be a good idea to downcase everything first?

# This is stuff I used for testing
binding.pry
# test = keywords.to_a
# test2 = []
# test.each do |x|
#   test2 << x[1]
# end
# puts test2.max