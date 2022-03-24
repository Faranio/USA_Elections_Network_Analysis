"""
Requirements to run this script:

- Install twint package
	+ Local machine: pip install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
	+ Virtual environment: pip install --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
	
- Uncomment the line 92 in url.py script of the twint package
"""

import twint


def collect_tweets(keyword, since, until, limit, min_likes, output_file):
	c = twint.Config()
	c.Search = keyword
	c.Since = since
	c.Until = until
	c.Count = True
	c.Lang = 'en'
	c.Limit = limit
	c.Min_likes = min_likes
	c.Store_csv = True
	c.Output = output_file
	
	twint.run.Search(c)


if __name__ == "__main__":
	collect_tweets(
		keyword='trump',
		since='2020-10-01',
		until='2020-11-03',
		limit=5000,
		min_likes=5000,
		output_file='trump.csv'
	)
	
	collect_tweets(
		keyword='biden',
		since='2020-10-01',
		until='2020-11-03',
		limit=5000,
		min_likes=5000,
		output_file='biden.csv'
	)
