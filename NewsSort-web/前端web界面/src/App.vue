<template>
	<div class="background">
		<el-card class="padding:3px" :style="back">
			<div class="title">
				NewsSort-新闻智分系统
			</div>
			<div class="tip">
				请输入新闻标题:
			</div>
			<el-input v-model="title" type="textarea" :rows="1" placeholder="请输入新闻标题" />
			<div class="tip">
				请输入新闻正文:
			</div>
			<el-input v-model="body" type="textarea" :rows="18" placeholder="请输入新闻正文内容" />
			<div>
				<el-button class="el-button" slot="trigger" icon="el-icon-help" size="medium" type="primary"
					@click="post_analyse()" round>
					新闻分类
				</el-button>
			</div>
			<div ref="analy" class="result">新闻类别：{{label}} </div>
		</el-card>
	</div>
</template>

<script>
	import axios from "axios";
	import bgimg from '/src/assets/background.png'
	export default {
		data() {
			return {
				title: '',
				body: '',
				show: 'hidden',
				label: '',
				back: {
					backgroundImage: 'url(' + bgimg + ')',
					backgroundRepeat:'no-repeat',
					backgroundSize:'100% 100%',
				}
			}
		},
		methods: {
			post_analyse() {
				var that = this;
				var title = that.title; // 获取输入框输入的新闻标题
				var body = that.body; // 获取输入框输入的新闻正文内容
				if (title == '' || body == '') {
					this.$message({
						showClose: true,
						message: '输入新闻内容不能为空!',
						type: 'warning'
					});
					that.label = '';
					that.$refs.analy.style.visibility = 'hidden'
				} else {
					axios.post('http://127.0.0.1:8000/newssort', {
						title: that.title,
						body: that.body
					}).then((response) => {
						console.log(response);
						console.log(response.data);
						that.label = response.data.label;
						that.$refs.analy.style.visibility = 'visible'
						that.$message({
							showClose: true,
							message: '新闻分类完成！ 新闻类别：' + that.label,
							type: 'success'
						});
					}).catch((error) => {
						console.log(error);
						that.$message({
							showClose: true,
							message: '请求出错！',
							type: 'error'
						});
					});
				}
			}
		}
	}
</script>

<style scoped>
	.background {
		width: 100%;
		height: 100%;
	}

	.title {
		font-family:cursive;
		font-size: 30px;
		font-weight: bold;
		margin: 0 auto;
		width: 325px;
		height: 35px;
		margin-bottom: 10px;
	}

	.tip {
		font-family: 宋体;
		font-size: 18px;
		font-weight: bold;
		margin-top: 20px;
		margin-bottom: 20px;
	}

	.el-button {
		margin: 0 auto;
		position: relative;
		margin-top: 15px;
		margin-bottom: 10px;
		display: block;
	}

	.result {
		font-family: 宋体;
		font-size: 22px;
		font-weight: bold;
		margin: 0 auto;
		margin-top: 15px;
		margin-bottom: 15px;
		width: 170px;
		height: 25px;
		color: #4876FF;
		visibility: hidden;
	}
</style>
