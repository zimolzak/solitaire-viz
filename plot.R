library(ggplot2)
# packageVersion('ggplot2')
X = read.csv("C:/Users/vhabhszimola/Documents/local/solitaire_viz/intermediate.csv", header=FALSE, stringsAsFactors=FALSE)

v = (X[18,])
j1_idx = 0
j2_idx = 0

for(i in c(1:length(v))){
  if(v[i] == " 'j2'"){
    j2_idx = i
    v[i] = 0
  }
  else if(v[i] == " 'j1'"){
    j1_idx = i
    v[i] = 0
  }
  else{
    v[i] = as.numeric(v[i])
  }
}

ts = data.frame(t(v), pos = c(1:54))
ggplot(ts, aes(pos, X18)) + geom_bar(stat='identity', width=1) + geom_vline(xintercept = j1_idx) + geom_vline(xintercept = j2_idx)
