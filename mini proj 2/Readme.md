WORD SENSE DISAMBIGUATION (WSD): find the correct meaning of a word given context

Data: English Lexical Sample Task written by Mihalcea, Chklovski and Kilgarriff in the following link:
http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.153.8426

The training data specifies the correct sense of the target word providing its verbal context surrounding the target word. Each line of training data has the the following format. Note that sense-ids in the test data are all erased to 0 as those are what you should predict.
word.pos | sense-id | prev-context %% target %% next-context
• word is the original form of the target word for which we are to predict the sense. You
will use it to lookup the XML dictionary.
• pos is the POS where ‘n’, ‘v’, and ‘a’ stand for noun, verb, and adjective, respectively.
• sense-id is the integer number for the correct sense id defined in our dictionary.
• prev-context is the text given earlier than each of the target word occurrence.
• target is the actual occurrence of the target word. Note that the word “begin.v” could occur as “beginning” instead of “begin” to denote a participle at the given position.
• next-context is the text given later than each of the target word occurrence.


Objectives
• Implement a WSD system by using two different models: ontological model and supervised model.
• A simple probabilistic approach called the Naive-Bayes model is deployed. The model takes a word in context as an input and outputs a probability distribution over predefined senses, indicating how likely each sense would be the correct meaning of the target word within the given context.
• Train the model and generate a output file consisting only of the predicted sense-ids
• Implement either add-1 or add-λ smoothing to achieve high quality performance 
