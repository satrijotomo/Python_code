
# Working with data from Hacker News
In this project, I am working with a dataset of submissions to Hacker News from 2006 to 2015. Hacker News is a site where users can submit articles from across the internet (usually about technology and startups), and others can "upvote" the articles, signifying that they like them. The more upvotes a submission gets, the more popular it was in the community. Popular articles get to the "front page" of Hacker News, where they're more likely to be seen by others.

The dataset was compiled by Arnaud Drizard using the Hacker News API, and can be found at https://github.com/arnauddri/hn. There are 10000 rows from the data randomly, and removed all extraneous columns. Hence, Our dataset only has four columns:

submission_time -- when the story was submitted.
upvotes -- number of upvotes the submission got.
url -- the base domain of the submission.
headline -- the headline of the submission. Users can edit this, and it doesn't have to match the headline of the original article.
