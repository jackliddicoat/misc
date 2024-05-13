# setwd
df <- readr::read_csv('sat.csv')
df$total <- df$vsat + df$msat
head(df)

min(df$total); median(df$total); mean(df$total); max(df$total)
hist(df$total, probability = T)
lines(density(df$total))
plot(density(df$vsat), col = "blue")
lines(density(df$msat), col = "red")
legend("topleft", legend = c("vsat", "msat"),
       col = c("blue", "red"), lty = 1)

mean(df$vsat); mean(df$msat)
sd(df$vsat); sd(df$msat)
t.test(df$msat, df$vsat, var.equal = T)
t.test(df$msat, df$vsat, var.equal = F)
# the means are statistically different

plot(msat ~ vsat, data = df, xlim = c(200, 800),
     ylim = c(200, 800), las = 1)
reg <- lm(msat ~ vsat, data = df)
abline(reg, col = "red", lty = 2)
summary(reg)$r.squared
text(x = 700, y = 300, expression(R^2 == .17))

summary(reg)$coefficients
plot(reg$residuals ~ reg$fitted.values)
abline(h=0, lty = 2, col = "red")
car::qqPlot(reg)
lmtest::bptest(reg)

df$mth_better <- ifelse(df$msat > df$vsat, 1, 0)
mth_stu <- subset(df, df$mth_better == 1)
ver_stu <- subset(df, df$mth_better == 0)
plot(msat ~ vsat, data = df, xlim = c(200, 800),
     ylim = c(200, 800))
points(mth_stu, col = "red")
points(ver_stu, col = "blue")
abline(a = 0, b = 1, lty = 2)

# about 5% of students scored higher than 700 on math
length(df$msat[df$msat > 700])/length(df$msat)

# about 5% of students scored higher than 650 on verbal
length(df$vsat[df$vsat > 650])/length(df$vsat)

# cumulative densities
cum_dist_m <- sort(cume_dist(df$msat)); msat_ord <- sort(df$msat)
cum_dist_v <- sort(cume_dist(df$vsat)); vsat_ord <- sort(df$vsat)
plot(cum_dist_m ~ msat_ord, type = "l", xlim = c(200, 800),
     col = "red", las = 1, xlab = "score", ylab="cumulative density")
lines(cum_dist_v ~ vsat_ord, col = "blue")
legend("topleft", legend = c("verbal", "math"),
       col = c("blue", "red"), lty = 1, cex = 1.1)


