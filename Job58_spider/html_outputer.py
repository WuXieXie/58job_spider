# coding:utf8
class HtmlOutput(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    #打印本地html表格
    def output_html(self):
        # 打开文件output.html 权限为write
        fout = open('output.html','w')
        print('success in')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        fout.write('<tr>')
        fout.write('<td>序号</td>')
        fout.write('<td>链接</td>')
        fout.write('<td>标题</td>')
        fout.write('<td>薪资</td>')
        fout.write('<td>公司名称</td>')
        fout.write('<td>描述</td>')
        fout.write('</tr>')

        count = 1
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%d</td>' % count)
            fout.write('<td>%s</td>' % data['Url'])
            fout.write('<td>%s</td>' % data['Title'])
            fout.write('<td>%s</td>' % data['Price'])
            fout.write('<td>%s</td>' % data['Company'])
            fout.write('<td>%s</td>' % data['Describle'])
            fout.write('</tr>')
            count = count + 1
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
