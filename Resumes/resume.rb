# These are Ruby gems. The first allows reading of PDFs, the second is for testing
require "pdf-reader"
require "pry"
require "stopwords"
require 'tesseract'

@tesseract = Tesseract::Engine.new {|e|
  e.language  = :eng
  e.blacklist = '|'
}

# This is an array of stop words
# The @ symbol means it is an instance variable, rather than a local variable
# So methods have access to it
@stopwords = Stopwords::STOP_WORDS

# This stores the path of all the resumes in the nonanalytics folder
resumes = Dir["Analytics/Intro to Analytics/MSiA 400 Resumes/Resume Packet UTenn/*"]

# Instantiates an empty hash
# A hash is a key: value pair
# So it will store the keywords and their counts
@keywords = {}

# This is a method that looks through a resume and updates the @keywords hash
def keyword_search(path_name)
  # This loads a PDF as a Ruby object
  reader = PDF::Reader.new(path_name)

  # Some resumes may be more than one page
  # So just loop through the reader.pages array
  text = ""

  # This sets text as a string of all the text in a resume
  reader.pages.each do |pp|
    text = text + " "
    text = text + pp.text
  end

  # text = @tesseract.text_for(path_name).strip

  # Replaces , ( ) with empty strings
  # What are some other symbols?
  # &, -
  ## Also stop words
  text.gsub!(",","")
  text.gsub!("(","")
  text.gsub!(")","")
  text.gsub!("[","")
  text.gsub!("]","")
  text.downcase!
  # This ● is throwing an error
  # But it works in pry for some reason
  # text.gsub!("●","")

  # Turns string into an array
  # It splits on the spaces (" ")
  arr = text.split

  # Loops through array
  # If keyword is present, adds 1 to the counter
  # If not present, instantiates it with a count of 1
  # binding.pry
  arr.each do |word|
    if @stopwords.include?("#{word}") == false
      if @keywords.has_key?(:"#{word}")
        @keywords[:"#{word}"] = @keywords[:"#{word}"] + 1
      else
        @keywords[:"#{word}"] = 1
      end
    end
  end
end

# This loops through all the resumes and calls the keyword_search method
resumes.each do |r|
  keyword_search(r)
end
# binding.pry
# This sorts the keywords by value
@keywords = @keywords.sort_by {|key, value| value}

# Prints keywords and their count to the screen
# Creates a new .txt file and prints the keys and values to that file
@f = File.new("utenn.txt", "w")
@keywords.each do |key, value|
  # puts "#{key}: #{value}"
  @f.write("#{key}\t#{value}\n")
end
@f.close



# My resume, somehow, doesn't use any words twice. Or I have an error somewhere.
### I had an error, but I think it's fixed

# It may be a good idea to downcase everything first?
# There are a lot of extra characters in the results

# This is stuff I used for testing
# binding.pry
# test = keywords.to_a
# test2 = []
# test.each do |x|
#   test2 << x[1]
# end
# puts test2.max