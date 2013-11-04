# These are Ruby gems. The first allows reading of PDFs, the second is for testing
require "pdf-reader"
require "pry"
require "stopwords"
require 'tesseract'

# Sets up tesseract gem
# This is for OCR
@tesseract = Tesseract::Engine.new {|e|
  e.language  = :eng
  e.blacklist = '|'
}

# This is an array of stop words
# The @ symbol means it is an instance variable, rather than a local variable
# So methods have access to it
@stopwords = Stopwords::STOP_WORDS

# This stores the path of all the resumes in the nonanalytics folder
resumes = Dir["Analytics/Intro to Analytics/MSiA 400 Resumes/Betas as PNG/*"]

# Instantiates an empty hash
# A hash is a key: value pair
# So it will store the keywords and their counts
@keywords = {}

# This is a method that looks through a resume and updates the @keywords hash
def keyword_search(path_name)
  # This loads a PDF as a Ruby object
  # reader = PDF::Reader.new(path_name)

  # Some resumes may be more than one page
  # So just loop through the reader.pages array
  # text = ""

  # # This sets text as a string of all the text in a resume
  # reader.pages.each do |pp|
  #   text = text + " "
  #   text = text + pp.text
  # end

  # Sets text as the OCR extracted text
  text = @tesseract.text_for(path_name).strip

  # Replaces , ( ) [ ]with empty strings
  # What are some other symbols?
  # &, -
  # Also makes everything lower case
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

  # This flags any resumes that don't contain 'and' or 'the'
  # if !(arr.include?("and") || arr.include?("the"))
  #   puts path_name
  # end

  # These remove the stopwords from the arr array
  # @stopwords.each do |s|
  #   arr.delete(s)
  # end

  # Sets the word array to be all pairs in the arr array
  # word_array = []
  # for i in 0..arr.length-2
  #   word_array << arr[i] + "_" + arr[i+1]
  # end

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

# This sorts the keywords by value
@keywords = @keywords.sort_by {|key, value| value}

# Prints keywords and their count to the screen
# Creates a new .txt file and prints the keys and values to that file
@f = File.new("betas_keyword_count.txt", "w")
@keywords.each do |key, value|
  # puts "#{key}: #{value}"
  @f.write("#{key}\t#{value}\n")
end
@f.close

# There are a lot of extra characters in the results