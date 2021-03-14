-- create constraints

ALTER TABLE dbo.Movies 
ADD UNIQUE (id)

ALTER TABLE dbo.Movies 
ADD UNIQUE (imdb_id)

ALTER TABLE [dbo].[Movies]  WITH CHECK 
ADD CONSTRAINT [inRange_budget] CHECK (budget>=0)

ALTER TABLE [dbo].[Movies]  WITH CHECK 
ADD CONSTRAINT [inRange_revenue] CHECK (revenue>=0)

ALTER TABLE [dbo].[Movies]  WITH CHECK 
ADD CONSTRAINT [inRange_popularity] CHECK (popularity>=0),
    CONSTRAINT [inRange_runtime] CHECK (runtime>=0)

ALTER TABLE [dbo].[Movies]  WITH CHECK 
ADD CONSTRAINT [inRange_is_adult] CHECK (is_adult in (0,1))

ALTER TABLE [dbo].[Critic]  WITH CHECK 
ADD CONSTRAINT [inRange_critic_score] CHECK (critic_score <= 100)

ALTER TABLE [dbo].[IMDB]  WITH CHECK 
ADD CONSTRAINT [inRange_average_rating] CHECK (average_rating>= 0 and average_rating<= 10)