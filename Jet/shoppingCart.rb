def solution(requests)
    r = Hash.new(0)
    requests.each do |x|
        t = x.split(":").map{|x| x.split(' ').join(' ')}
        case t[0]
        when "add"
            r[t[1]] += 1
        when "remove"
            r.delete(t[1])
        when "checkout"
            r.clear
        when "quantity_upd"
            k = t[-1].split('')
            n = k[1..-1].join.to_i
            if k.first == '+'
                r[t[1]] += n
            elsif k.first == '-'
                r[t[1]] -= n
            end
        end
    end
    res = []
    r.each do |x, y|
        res << "#{x} : #{y}"
    end
    res
end