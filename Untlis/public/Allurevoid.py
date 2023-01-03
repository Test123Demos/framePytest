import allure

class Allurevoid():
    def attach_text(self,body, name, attachment_type=allure.attachment_type.TEXT):
        """
        附件为内容
        """
        allure.attach(body, name, attachment_type=attachment_type)

    def attach_file(self,filePath, name, attachment_type=allure.attachment_type.TEXT):
        """
        附件为文件
        CSV、HTML、XML、JSON、YAML、PCAP、PNG、JPG、SVG、GIF、BMP、MP4、OGG、WEBM、PDF
        """

        allure.attach.file(filePath, name, attachment_type=attachment_type)

