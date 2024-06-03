library(Stat2Data)

data("YouthRisk2009")

YouthRisk2009 %>% 
  View()

mj.age <- glm(YouthRisk2009$MarijuaEver ~ YouthRisk2009$Age, family = "binomial")

summary(mj.age)
exp(mj.age$coefficients[2]) - 1

exp(confint((mj.age)))

# a year increase in age increases the odds of ever having smoked weed
# by ~38%, 95% CI [1.18, 1.62]



?YouthRisk2009


## percentage of the sample that has smoked marijuana ever

dim(YouthRisk2009) ## get the number of rows and cols

ifelse(YouthRisk2009$MarijuaEver=="Yes", 1, 0)
## This makes it such that the answer "yes" to whether a person has ever smoked
## mj is equal to 1, 0 if not

## does having ever smoked mj affect sleep?

yr.glm <- glm(Sleep7 ~ MarijuaEver, data = YouthRisk2009, family = "binomial")
summary(yr.glm)

## marijuana has no effect on whether a person got 7 hrs of sleep or not
## people who smoked were 28% less likely to get 7hr of sleep, but this
## was statistically insignificant: 95% CI [0.48, 1.08]
exp(yr.glm$coefficients[2])
exp(confint(yr.glm))

YouthRisk2009$SmokeDaily <- ifelse(YouthRisk2009$SmokeDaily=="Yes", 1, 0)

## did people who smoked daily get less than 7hr of sleep
yr.glm2 <- glm(Sleep7 ~ SmokeDaily, data = YouthRisk2009, family = "binomial")
summary(yr.glm2)

## yes, they did!
exp(-1.4407) - 1
## People who smoked daily got were 76% less likely to get 7hr of sleep
## OR = 0.24
emplogitplot1(Sleep7 ~ SmokeDaily, data = YouthRisk2009, ngroups = 2,
              xlab = ("Smoke Daily? (1=yes, 0=no)"),
              main = "Log odds of at least 7hr of sleep, smokers vs non-smokers")
exp(confint(yr.glm2))
## 95% CI: [0.11, 0.46]

