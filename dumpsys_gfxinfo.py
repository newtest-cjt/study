# -*- coding: UTF-8 -*-

import os


short_name = "包名"
pid = os.popen("adb shell ps | grep " + short_name).read().split()[1]
# os.popen("adb shell am start yuside.cn.numbersonly/yuside.cn.numbersonly.MainActivity")
# time.sleep(5)
if len(pid) != 0:
    cmd_gfx = "adb shell dumpsys gfxinfo " + pid
    print(cmd_gfx)
    fps_lines = os.popen(cmd_gfx).read().split("\n")
    for i in fps_lines:
        print(i)
    count_infos = len(fps_lines)
    start_line = 0

    jank_count = 0
    vsync_overtime = 0
    frame_count = 0
    # 发现丢帧直接跳过下一帧
    jump = 0
    for i in range(count_infos):
        # print(fps_lines[i]+"02")
        if "Draw"in fps_lines[i] and "Process" in fps_lines[i] and "Execute" in fps_lines[i]:
            start_line = i + 128
            continue
        if i < start_line:
            time_block = fps_lines[i].split()
            # print(str(time_block)+"03")
            render_time = 0
            try:
                for ti in time_block:
                    render_time += float(ti)
            except Exception as e:
                continue
            frame_count += 1
            '''
               获取方式：
               pid = adb shell ps | grep
               adb shell dumpsys gfxinfo pid
               当渲染时间大于16.67，按照垂直同步机制，该帧就已经渲染超时
               那么，如果它正好是16.67的整数倍，比如66.68，则它花费了4个垂直同步脉冲，减去本身需要一个，则超时3个
               如果它不是16.67的整数倍，比如67，那么它花费的垂直同步脉冲应向上取整，即5个，减去本身需要一个，即超时4个，可直接算向下取整

               最后的计算方法思路：
               执行一次命令，总共收集到了m帧（理想情况下m=128），但是这m帧里面有些帧渲染超过了16.67毫秒，算一次jank，一旦jank，
               需要用掉额外的垂直同步脉冲。其他的就算没有超过16.67，也按一个脉冲时间来算（理想情况下，一个脉冲就可以渲染完一帧）

               所以FPS的算法可以变为：
               m / （m + 额外的垂直同步脉冲） * 60
            '''
            if render_time > 16.67:
                jank_count += 1
                if render_time % 16.67 == 0:
                    vsync_overtime += int(render_time / 16.67) - 1
                else:
                    vsync_overtime += int(render_time / 16.67)

    fps = int(frame_count * 60 / (frame_count + vsync_overtime))
    print("frame_count-jank_count-FPS: " + str(frame_count) + "-" + str(jank_count) + "-" + str(fps))
